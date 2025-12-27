"use client"

import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from "@/components/ui/dialog"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import type { User } from "@/lib/types"
import { Mail, Shield, User as UserIcon } from "lucide-react"

export function UserProfileModal({
  user,
  open,
  onOpenChange,
}: {
  user: User | null
  open: boolean
  onOpenChange: (v: boolean) => void
}) {
  if (!user) return null

  const initials = (user.username || "U").slice(0, 1).toUpperCase()

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-lg">
        <DialogHeader>
          <DialogTitle>Profile</DialogTitle>
          <DialogDescription>Your account details</DialogDescription>
        </DialogHeader>

        <div className="flex items-center gap-4">
          <div className="h-14 w-14 rounded-full bg-[#f5c842] text-[#1a2c5b] flex items-center justify-center text-2xl font-bold">
            {initials}
          </div>
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <h3 className="text-lg font-semibold text-gray-900 truncate">{user.username}</h3>
              <Badge className="bg-[#1a2c5b] text-white hover:bg-[#1a2c5b]">
                {user.role?.toUpperCase?.() ?? "USER"}
              </Badge>
            </div>
            <p className="text-sm text-gray-500 truncate">{user.email}</p>
          </div>
        </div>

        <div className="grid gap-3 mt-4">
          <Card>
            <CardContent className="p-4 space-y-3">
              <div className="flex items-center gap-3">
                <UserIcon className="h-4 w-4 text-gray-500" />
                <div className="flex-1 flex items-center justify-between gap-4">
                  <span className="text-sm text-gray-600">Username</span>
                  <span className="text-sm font-medium text-gray-900">{user.username}</span>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <Mail className="h-4 w-4 text-gray-500" />
                <div className="flex-1 flex items-center justify-between gap-4">
                  <span className="text-sm text-gray-600">Email</span>
                  <span className="text-sm font-medium text-gray-900">{user.email}</span>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <Shield className="h-4 w-4 text-gray-500" />
                <div className="flex-1 flex items-center justify-between gap-4">
                  <span className="text-sm text-gray-600">Role</span>
                  <span className="text-sm font-medium text-gray-900">{user.role}</span>
                </div>
              </div>
            </CardContent>
          </Card>

          <p className="text-xs text-gray-500">
            (Future) You can add “Edit Profile” here when backend is ready.
          </p>
        </div>
      </DialogContent>
    </Dialog>
  )
}
